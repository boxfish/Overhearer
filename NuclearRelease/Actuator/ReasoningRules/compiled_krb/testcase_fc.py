# testcase_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.0.4'
compiler_version = 1

def has_intention_to(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'int_status', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'has_intention',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_intention_that(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'int_status', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'has_intention',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def parent_of_action(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'subaction_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'parent_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def parent_of_parameter(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'param_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'parent_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('plangraph', 'ancestor_of',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_grand(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'parent_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('plangraph', 'ancestor_of',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ancestor_of_ancestor(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'parent_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'ancestor_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('plangraph', 'ancestor_of',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def belief_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('plangraph', 'has_intention', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('plangraph', 'ancestor_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('plangraph', 'value_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('plangraph', 'generated_value_of', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('value1') == context.lookup_data('value2'):
                      engine.assert_('plangraph', 'belief_value_of',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),
                                      rule.pattern(2).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def inform_belief_value_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('test', 'case_number', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('case') in [1, 2, 3, 4, 5, 6]:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('plangraph', 'belief_value_of', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('geocontent', 'type_of', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  with knowledge_base.Gen_once if index == 3 \
                           else engine.lookup('plangraph', 'param_of', context,
                                              rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      with knowledge_base.Gen_once if index == 4 \
                               else engine.lookup('plangraph', 'status_of', context,
                                                  rule.foreach_patterns(4)) \
                        as gen_4:
                        for dummy in gen_4:
                          if context.lookup_data('status') != 'exec_success':
                            engine.assert_('maprole', 'inform_belief_value_of',
                                           (rule.pattern(0).as_data(context),
                                            rule.pattern(1).as_data(context),
                                            rule.pattern(2).as_data(context),)),
                            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def contextualize_action(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('test', 'case_number', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('case') in (4, 5, 6):
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('plangraph', 'has_intention', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('plangraph', 'context_of', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  with knowledge_base.Gen_once if index == 3 \
                           else engine.lookup('plangraph', 'status_of', context,
                                              rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      if context.lookup_data('status') != 'exec_success':
                        engine.assert_('maprole', 'contextualize_action',
                                       (rule.pattern(0).as_data(context),
                                        rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'inform_belief_value_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('maptask', 'locate',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def background(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maprole', 'contextualize_action', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('geocontent', 'type_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('maptask', 'background',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('test', 'case_number', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('case') in [1, 4]:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('maptask', 'locate', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('mapview', 'scale_level',
                             (rule.pattern(0).as_data(context),)),
              engine.assert_('mapview', 'marker',
                             (rule.pattern(1).as_data(context),)),
              engine.assert_('mapview', 'label',
                             (rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('test', 'case_number', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('case') in [2, 5]:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('maptask', 'locate', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('mapview', 'scale_level',
                             (rule.pattern(0).as_data(context),)),
              engine.assert_('mapview', 'center',
                             (rule.pattern(1).as_data(context),)),
              engine.assert_('mapview', 'label',
                             (rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def locate_stra_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('test', 'case_number', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('case') in [3, 6]:
          with knowledge_base.Gen_once if index == 1 \
                   else engine.lookup('maptask', 'locate', context,
                                      rule.foreach_patterns(1)) \
            as gen_1:
            for dummy in gen_1:
              engine.assert_('mapview', 'scale_level',
                             (rule.pattern(0).as_data(context),)),
              engine.assert_('mapview', 'marker',
                             (rule.pattern(1).as_data(context),)),
              engine.assert_('mapview', 'label',
                             (rule.pattern(1).as_data(context),)),
              engine.assert_('mapview', 'center',
                             (rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def background_stra(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('maptask', 'background', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('mapview', 'layer',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('testcase')
  
  fc_rule.fc_rule('has_intention_to', This_rule_base, has_intention_to,
    (('plangraph', 'int_status',
      (contexts.variable('agent'),
       contexts.variable('action'),
       pattern.pattern_literal('int_intendTo'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('has_intention_that', This_rule_base, has_intention_that,
    (('plangraph', 'int_status',
      (contexts.variable('agent'),
       contexts.variable('action'),
       pattern.pattern_literal('int_intendThat'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('parent_of_action', This_rule_base, parent_of_action,
    (('plangraph', 'subaction_of',
      (contexts.variable('subaction'),
       contexts.variable('plannode'),),
      False),),
    (contexts.variable('plannode'),
     contexts.variable('subaction'),))
  
  fc_rule.fc_rule('parent_of_parameter', This_rule_base, parent_of_parameter,
    (('plangraph', 'param_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('action'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('ancestor_of_parent', This_rule_base, ancestor_of_parent,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),),
    (contexts.variable('parent'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('ancestor_of_grand', This_rule_base, ancestor_of_grand,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),
     ('plangraph', 'parent_of',
      (contexts.variable('grand'),
       contexts.variable('parent'),),
      False),),
    (contexts.variable('grand'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('ancestor_of_ancestor', This_rule_base, ancestor_of_ancestor,
    (('plangraph', 'parent_of',
      (contexts.variable('parent'),
       contexts.variable('son'),),
      False),
     ('plangraph', 'ancestor_of',
      (contexts.variable('ancestor'),
       contexts.variable('parent'),),
      False),),
    (contexts.variable('ancestor'),
     contexts.variable('son'),))
  
  fc_rule.fc_rule('belief_value_of', This_rule_base, belief_value_of,
    (('plangraph', 'has_intention',
      (contexts.variable('agent'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'ancestor_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'value_of',
      (contexts.variable('value1'),
       contexts.variable('param'),),
      False),
     ('plangraph', 'generated_value_of',
      (contexts.variable('value2'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('value1'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('inform_belief_value_of', This_rule_base, inform_belief_value_of,
    (('test', 'case_number',
      (contexts.variable('case'),),
      False),
     ('plangraph', 'belief_value_of',
      (contexts.variable('agent'),
       contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (contexts.anonymous('_'),
       contexts.variable('value'),),
      False),
     ('plangraph', 'param_of',
      (contexts.variable('param'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('agent'),
     contexts.variable('value'),
     contexts.variable('param'),))
  
  fc_rule.fc_rule('contextualize_action', This_rule_base, contextualize_action,
    (('test', 'case_number',
      (contexts.variable('case'),),
      False),
     ('plangraph', 'has_intention',
      (contexts.variable('agent'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'context_of',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('plangraph', 'status_of',
      (contexts.variable('status'),
       contexts.variable('action'),),
      False),),
    (contexts.variable('value'),
     contexts.variable('action'),))
  
  fc_rule.fc_rule('locate', This_rule_base, locate,
    (('maprole', 'inform_belief_value_of',
      (contexts.variable('agent'),
       contexts.variable('value'),
       contexts.variable('param'),),
      False),
     ('geocontent', 'type_of',
      (pattern.pattern_literal('location'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),))
  
  fc_rule.fc_rule('background', This_rule_base, background,
    (('maprole', 'contextualize_action',
      (contexts.variable('value'),
       contexts.variable('action'),),
      False),
     ('geocontent', 'type_of',
      (pattern.pattern_literal('layer'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('value'),))
  
  fc_rule.fc_rule('locate_stra_1', This_rule_base, locate_stra_1,
    (('test', 'case_number',
      (contexts.variable('case'),),
      False),
     ('maptask', 'locate',
      (contexts.variable('value'),),
      False),),
    (pattern.pattern_literal('state'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('locate_stra_2', This_rule_base, locate_stra_2,
    (('test', 'case_number',
      (contexts.variable('case'),),
      False),
     ('maptask', 'locate',
      (contexts.variable('value'),),
      False),),
    (pattern.pattern_literal('local'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('locate_stra_3', This_rule_base, locate_stra_3,
    (('test', 'case_number',
      (contexts.variable('case'),),
      False),
     ('maptask', 'locate',
      (contexts.variable('value'),),
      False),),
    (pattern.pattern_literal('county'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('background_stra', This_rule_base, background_stra,
    (('maptask', 'background',
      (contexts.variable('value'),),
      False),),
    (contexts.variable('value'),))


Krb_filename = '../testcase.krb'
Krb_lineno_map = (
    ((13, 17), (4, 4)),
    ((18, 20), (6, 6)),
    ((29, 33), (10, 10)),
    ((34, 36), (12, 12)),
    ((45, 49), (16, 16)),
    ((50, 52), (18, 18)),
    ((61, 65), (22, 22)),
    ((66, 68), (24, 24)),
    ((77, 81), (28, 28)),
    ((82, 84), (30, 30)),
    ((93, 97), (34, 34)),
    ((98, 102), (35, 35)),
    ((103, 105), (37, 37)),
    ((114, 118), (41, 41)),
    ((119, 123), (42, 42)),
    ((124, 126), (44, 44)),
    ((135, 139), (48, 48)),
    ((140, 144), (49, 49)),
    ((145, 149), (50, 50)),
    ((150, 154), (51, 51)),
    ((155, 155), (52, 52)),
    ((156, 159), (54, 54)),
    ((168, 172), (59, 59)),
    ((173, 173), (60, 60)),
    ((174, 178), (61, 61)),
    ((179, 183), (62, 62)),
    ((184, 188), (63, 63)),
    ((189, 193), (64, 64)),
    ((194, 194), (65, 65)),
    ((195, 198), (67, 67)),
    ((207, 211), (71, 71)),
    ((212, 212), (72, 72)),
    ((213, 217), (73, 73)),
    ((218, 222), (74, 74)),
    ((223, 227), (75, 75)),
    ((228, 228), (76, 76)),
    ((229, 231), (78, 78)),
    ((240, 244), (83, 83)),
    ((245, 249), (84, 84)),
    ((250, 251), (86, 86)),
    ((260, 264), (90, 90)),
    ((265, 269), (91, 91)),
    ((270, 271), (93, 93)),
    ((280, 284), (98, 98)),
    ((285, 285), (99, 99)),
    ((286, 290), (100, 100)),
    ((291, 292), (102, 102)),
    ((293, 294), (103, 103)),
    ((295, 296), (104, 104)),
    ((305, 309), (108, 108)),
    ((310, 310), (109, 109)),
    ((311, 315), (110, 110)),
    ((316, 317), (112, 112)),
    ((318, 319), (113, 113)),
    ((320, 321), (114, 114)),
    ((330, 334), (118, 118)),
    ((335, 335), (119, 119)),
    ((336, 340), (120, 120)),
    ((341, 342), (122, 122)),
    ((343, 344), (123, 123)),
    ((345, 346), (124, 124)),
    ((347, 348), (125, 125)),
    ((357, 361), (129, 129)),
    ((362, 363), (131, 131)),
)
